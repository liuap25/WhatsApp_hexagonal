# WhatsApp Cloud API - Configuración y Envio de Mensajes

Este documento proporciona una guía paso a paso para configurar **WhatsApp Cloud API** y enviar mensajes utilizando el número de prueba proporcionado por Meta.

---

## 🚀 Paso 1: Crear una cuenta en Meta for Developers
1. Ir a [Meta for Developers](https://developers.facebook.com/).
2. Iniciar sesión con tu cuenta de Facebook.
3. Ir a **Mis Apps** > **Crear App**.
4. Seleccionar el tipo de app **"Negocios"** y hacer clic en **Siguiente**.
5. Ingresar un **nombre para la app** y hacer clic en **Crear app**.
6. Completar la verificación de seguridad.

---

## 🔧 Paso 2: Agregar WhatsApp a la aplicación
1. En el panel de tu aplicación, ir a **Agregar un producto**.
2. Seleccionar **WhatsApp** y hacer clic en **Configurar**.
3. Elegir la cuenta de **Meta Business Manager** o crear una nueva.
4. En la sección **Configuración de la APi** > **Ajustes de WhatsApp**, aparecerá el **Token de acceso temporal**.

---

## 📲 Paso 3: Obtener el número de prueba de WhatsApp
1. Dentro de **WhatsApp Cloud API**, ir a la pestaña **Prueba de API**.
2. Copiar el **número de prueba** proporcionado por Meta.
3. Agregar un número de teléfono (tu número personal) como **Destinatario** para hacer pruebas.

---

# Configuración de Webhook para WhatsApp con Ngrok

Este documento describe los pasos para configurar un Webhook para recibir métricas de WhatsApp utilizando **Ngrok**.

---

## 🚀 Paso 1: Crear una cuenta en Ngrok

1. Ir a [Ngrok](https://ngrok.com/) y crear una cuenta.
2. Verificar tu cuenta a través del correo electrónico.
3. Iniciar sesión y obtener el **Authtoken** desde el panel de usuario.

---

## 🔧 Paso 2: Instalar y configurar Ngrok

### 🔹 **Windows**

1. Descargar el archivo `ngrok.exe` desde [Ngrok Downloads](https://ngrok.com/download).
2. Mover `ngrok.exe` a una carpeta accesible, por ejemplo, `C:\ngrok`.
3. Abrir la terminal (cmd o PowerShell) y navegar hasta la carpeta donde está `ngrok.exe`:
   ```sh
   cd C:\ngrok
   ```
4. Ingresar el token de autenticación:
   ```sh
   ngrok config add-authtoken YOUR_NGROK_AUTHTOKEN
   ```

### 🔹 **Linux y macOS**

1. Descargar Ngrok:
   ```sh
   wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
   ```
2. Extraer el archivo:
   ```sh
   unzip ngrok-stable-linux-amd64.zip
   ```
3. Mover Ngrok a `/usr/local/bin` para acceso global:
   ```sh
   sudo mv ngrok /usr/local/bin/
   ```
4. Ingresar el token de autenticación:
   ```sh
   ngrok config add-authtoken YOUR_NGROK_AUTHTOKEN
   ```

---

## 🌍 Paso 3: Ejecutar el túnel público con Ngrok

Para exponer un servidor local (por ejemplo, un API en **Flask** o **FastAPI** en el puerto 5000):

```sh
ngrok http http://localhost:8080
```

Al ejecutar este comando, aparecerá una salida similar a esta:

```sh
Forwarding                    https://random-subdomain.ngrok.io -> http://localhost:8080
```

Anota la URL `https://random-subdomain.ngrok.io`, ya que se usará para configurar el webhook en Meta.

---

## 🔗 Paso 4: Configurar el Webhook en Meta

1. Ir a [Meta Developers](https://developers.facebook.com/).
2. En la aplicación de WhatsApp, ir a **Configuración** > **Webhooks**.
3. Hacer clic en **Agregar Webhook** y pegar la URL de Ngrok (`https://random-subdomain.ngrok.io/webhook`).
4. Ingresar tu token secreto (puede ser cualquier nombre que deseas)
5. Seleccionar los eventos que deseas recibir (por ejemplo, `messages`, `status`, `metrics`).
6. Guardar los cambios.

---



