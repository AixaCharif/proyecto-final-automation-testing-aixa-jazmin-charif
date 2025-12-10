# 🧪 Proyecto Final – Automation Testing  

Este proyecto integra pruebas automatizadas de **interfaz web (UI)** y **API**, aplicando buenas prácticas de automatización, uso de fixtures, manejo de logs, reporte HTML y organización modular.  
Las pruebas fueron realizadas sobre el sitio **https://www.saucedemo.com** y una API simulada para operaciones CRUD de productos.

---

## 🎯 Objetivos del Proyecto
- Automatizar flujos completos en UI usando Selenium WebDriver.
- Implementar pruebas API utilizando `requests`.
- Aplicar Pytest con fixtures, parametrización y manejo de errores.
- Generar reportes HTML de ejecución.
- Incorporar logs detallados en cada prueba.
- Demostrar dominio de automatización y buenas prácticas.

---

## 📁 Estructura del Proyecto
```
proyecto-final/
│
├── config/
│   └── logging.conf
│
├── data/
│   └── user.json
│
├── pages/
│   ├── cart_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── reports/
│   ├── logs/
│   │   └── execution.log
│   ├── screenshots/
│   └── report.html
│
├── tests/
│   ├── test_add_to_cart.py
│   ├── test_api.py
│   ├── test_checkout.py
│   ├── test_inventory.py
│   ├── test_login.py
│   └── test_negative_login.py
│
├── utils/
│   ├── api_client.py
│   └── functions.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```
---

## ⚙️ Tecnologías utilizadas
- **Python 3.10+**
- **Selenium WebDriver**
- **Pytest**
- **Pytest-HTML**
- **Requests**
- **Google Chrome + ChromeDriver**
- **Logging**
- **Git / GitHub**

---

## 📦 Instalación de dependencias

- Clonar este repositorio:
    **git clone https://github.com/aixacharif/proyecto-final-automation-testing-aixa-jazmin-charif.git**

- Ingresar al directorio del proyecto:
    **cd proyecto-final-automation-testing-aixa-jazmin-charif**

- Instalar dependencias:
    **pip install -r requirements.txt**

---

## ▶️ Ejecución de las pruebas
 
Ejecutar los tests y generar un reporte HTML con Pytest:

**pytest -v --html=reports/report.html --self-contained-html**

El reporte HTML se generará en reports/report.html

---

### 📝 ¿Cómo interpretar los reportes generados?

El proyecto genera un reporte HTML automático mediante **pytest-html** ubicado en:

```
reports/report.html
```

Dentro del reporte vas a encontrar:

#### ✔️ Resumen general  
Muestra la cantidad de pruebas **PASSED**, **FAILED**, **SKIPPED** y su porcentaje.

#### ✔️ Detalle por prueba  
Para cada test se visualiza:
- Nombre del test  
- Resultado (PASSED / FAILED)  
- Tiempo de ejecución  
- Logs asociados

#### ✔️ Capturas de pantalla  
Cuando una prueba falla, se adjunta automáticamente una captura dentro de:
```
reports/screenshots/
```
y también aparece incrustada en el reporte HTML.

#### ✔️ Logs de ejecución  
Todos los eventos quedan registrados en:
```
reports/logs/execution.log
```
Contiene información detallada del flujo, ideal para depurar.
