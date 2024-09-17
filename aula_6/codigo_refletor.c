// Definindo pinos
const int pirSensor = 7;       // Pino do sensor PIR (entrada digital)
const int ledPin = 9;          // Pino do LED (PWM para controlar o brilho)
const int ldrPin = A1;         // Pino da LDR (entrada analógica)
const int pirPowerPin = 10;    // Pino que controla a alimentação do PIR (via LDR)
const int ldrThreshold = 500;  // Limite de luz para ativar o sistema (ajuste conforme necessário)

// Variáveis de estado
int ldrValue = 0;        // Valor lido pela LDR
int pirState = LOW;      // Estado atual do PIR
int previousPirState = LOW; // Estado anterior do PIR

// Variáveis de controle de tempo
unsigned long currentMillis = 0;
unsigned long ledTimer = 0;        // Temporizador para o LED (10 segundos)
unsigned long pirTimer = 0;        // Temporizador para o PIR (5 segundos)

const unsigned long ledOnDuration = 10000;  // Tempo de LED a 100% após pouca luz (10 segundos)
const unsigned long pirDuration = 5000;     // Duração de LED a 100% após movimento detectado pelo PIR

// Estado do LED
bool ledAtFullBrightness = true;  // Flag para saber se o LED está em 100%
bool systemActive = false;        // Flag para saber se o sistema está ativo
bool pirTriggered = false;        // Flag para saber se o PIR foi acionado

void setup() {
  // Configuração dos pinos
  pinMode(ledPin, OUTPUT);        // LED como saída
  pinMode(pirSensor, INPUT);      // PIR como entrada
  pinMode(pirPowerPin, OUTPUT);   // Controle do PIR
  pinMode(ldrPin, INPUT);         // LDR como entrada analógica

  // Inicializa comunicação serial para depuração
  Serial.begin(9600);
  Serial.println("Sistema iniciado.");
}

void loop() {
  // Atualiza o tempo atual
  currentMillis = millis();

  // Leitura da LDR
  ldrValue = analogRead(ldrPin);
  Serial.print("Valor da LDR: ");
  Serial.println(ldrValue);

  // Verifica se há pouca luz para ativar o sistema
  if (ldrValue < ldrThreshold) {
    if (!systemActive) {
      // Ativa o sistema pela primeira vez
      systemActive = true;
      digitalWrite(pirPowerPin, HIGH);  // Liga o PIR
      analogWrite(ledPin, 255);         // LED em 100% de brilho
      ledTimer = currentMillis;         // Reinicia o temporizador dos 10 segundos
      ledAtFullBrightness = true;       // Marca que o LED está em 100% de brilho
      pirTriggered = false;             // Reseta o estado do PIR
      Serial.println("Pouca luz detectada. LED em 100%.");
    }

    // Verifica se passaram 10 segundos desde o início da pouca luz
    if (ledAtFullBrightness && (currentMillis - ledTimer >= ledOnDuration)) {
      analogWrite(ledPin, 127);        // Reduz o brilho para 50% após 10 segundos
      ledAtFullBrightness = false;     // Marca que o LED não está mais em 100%
      Serial.println("LED reduzido para 50% após 10 segundos.");
    }

    // Controle do PIR
    pirState = digitalRead(pirSensor);
    if (pirState == HIGH && previousPirState == LOW) {
      Serial.println("Movimento detectado! LED em 100% por 5 segundos.");
      analogWrite(ledPin, 255);          // LED em 100% de brilho
      pirTimer = currentMillis;          // Reinicia o temporizador do PIR
      pirTriggered = true;               // Marca que o PIR foi acionado
    }
    previousPirState = pirState;

    // Se o PIR foi acionado, o LED permanece a 100% por 5 segundos
    if (pirTriggered) {
      if (currentMillis - pirTimer < pirDuration) {
        analogWrite(ledPin, 255);        // Garante que o LED fique a 100% por 5 segundos
      } else {
        analogWrite(ledPin, 127);        // Após 5 segundos, reduz o LED para 50%
        pirTriggered = false;            // Reseta a flag do PIR
        Serial.println("LED reduzido para 50% após detecção de movimento.");
      }
    }

  } else {
    // Se há claridade suficiente, desliga o sistema
    if (systemActive) {
      digitalWrite(pirPowerPin, LOW);      // Desliga o PIR
      analogWrite(ledPin, 0);              // Apaga o LED
      systemActive = false;                // Marca o sistema como inativo
      Serial.println("Muita luz detectada. Sistema desligado.");
    }
  }

  // Pequeno delay para evitar leituras excessivas
  delay(100);
}
