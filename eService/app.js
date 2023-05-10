const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.set("Content-Type", "text/html");
  res.send(`
  <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Page Title</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
        <script src='main.js'></script>
    </head>
    <body>
        <html>
    <head>
    </head>
    <body>
      <h1>Check out our smart widget!</h1>
      <iframe src="https://3cdb-213-182-133-198.ngrok-free.app" height="800" width="800" title="iframe Example" sandbox="allow-same-origin allow-top-navigation allow-forms allow-scripts"></iframe>
    </body>
  </html>`);
});

app.get("/redirect", (req, res) => {
  res.set("Content-Type", "text/html");
  res.send(`
  <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Page Title</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
        <script src='main.js'></script>
    </head>
    <body>
        <html>
    <head>
    </head>
    <body>
      <iframe src="https://3cdb-213-182-133-198.ngrok-free.app/not_installed" height="800" width="400" title="iframe Example" sandbox="allow-same-origin allow-top-navigation allow-forms allow-scripts"></iframe>
    </body>
  </html>`);
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});