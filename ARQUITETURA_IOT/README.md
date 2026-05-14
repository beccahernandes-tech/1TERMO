# Arquitetura IoT (Internet das Coisas)

## 📌 Ementa e Conteúdo de Aula
*   **Introdução à IoT:** Conceitos fundamentais, evolução histórica e impacto no mercado.
*   **Camadas da Arquitetura:** Sensor/Atuador (borda), Rede/Comunicação, Plataforma/Nuvem e Aplicação.
*   **Protocolos de Comunicação:** MQTT, HTTP, CoAP, LoRaWAN e Zigbee.
*   **Hardwares para IoT:** Microcontroladores, microprocessadores e topologias de rede sem fio.
*   **Computação em Névoa (Fog) e Borda (Edge):** Processamento de dados local versus nuvem.
*   **Segurança em IoT:** Criptografia de dados, autenticação de dispositivos e vulnerabilidades.

---

## 🤖 Ecossistema Arduino
*   **O que é:** Plataforma de prototipagem eletrônica de código aberto baseada em hardware e software livres.
*   **Componentes Principais:** Microcontrolador (ex: ATmega328P no Uno), pinos digitais/analógicos e interface USB.
*   **Sensores Comuns:** DHT11 (Temperatura/Umidade), LDR (Luminosidade), HC-SR04 (Ultrassônico).
*   **Atuadores Comuns:** Relés, servomotores, LEDs e buzzers.
*   **Placas IoT Dedicadas:** Arduino Nano 33 IoT, MKR WiFi 1010 e integração com módulos ESP8266/ESP32.

---

## 💻 Linguagens de Programação

### 1. Linguagem C++ (Programação de Dispositivos / Edge)
*   **Uso em IoT:** Utilizada diretamente na IDE do Arduino para controle de baixo nível e firmware.
*   **Vantagens:** Alta performance, controle direto do hardware e consumo otimizado de memória.
*   **Estrutura Básica do Código (Sketch):**
    ```cpp
    // Executa uma única vez ao ligar a placa
    void setup() {
      pinMode(13, OUTPUT); // Configura o pino 13 como saída
    }

    // Executa em loop infinito
    void loop() {
      digitalWrite(13, HIGH); // Liga o LED
      delay(1000);            // Aguarda 1 segundo
      digitalWrite(13, LOW);  // Desliga o LED
      delay(1000);            // Aguarda 1 segundo
    }
    ```

### 2. Linguagem Python (Gateway, Nuvem e Análise de Dados)
*   **Uso em IoT:** Executada em gateways (como Raspberry Pi) e servidores para processar dados dos sensores.
*   **Vantagens:** Sintaxe limpa, desenvolvimento rápido e ecossistema rico para Inteligência Artificial/Machine Learning.
*   **Bibliotecas Chave:** `Paho-MQTT` (comunicação), `Requests` (APIs HTTP), `Pandas` (análise de dados) e `RPI.GPIO` (controle de pinos).
*   **Exemplo de Cliente MQTT Simples:**
    ```python
    import paho.mqtt.client as mqtt
    import time

    client = mqtt.Client()
    client.connect("hivemq.com", 1883, 60)

    while True:
        # Simula o envio de um dado de temperatura
        client.publish("iot/arquitetura/temperatura", "25.4")
        print("Dado enviado com sucesso!")
        time.sleep(5)
    ```
