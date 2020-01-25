# Mauritius Sea Cable

The aim of this project is to provide a simple graphical user interface to show the Health Status of submarine cables connected to Mauritius.

![ProjectImage](https://github.com/MrSunshyne/mauritius-sea-cable/raw/master/public/images/og-image.jpg)

**[View the Live Website](https://mrsunshyne.github.io/mauritius-sea-cable/)**

> This project is inspired by the beautiful website [baliseacable.com](baliseacable.com)

## Data Source

The data source is yet to be made available.
It is expected to be in the following format :

```js
// file: all-servers.json
{
    LION : <SpeedtestResult>,
    MARS: <SpeedtestResult>,
    SAFE1:<SpeedtestResult>,
    SAFE2:<SpeedtestResult>,
    SAFE3:<SpeedtestResult>
}
// Where Speedtest result has the following signature
Interface SpeedtestResult {
    timestamp: '',
    upload: '',
    download: '',
    ping: ''
}
```

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```
