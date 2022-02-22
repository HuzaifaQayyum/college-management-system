const { app, BrowserWindow } = require('electron');
const path = require('path');


app.on('ready', () => {
    const splashWindow = new BrowserWindow({
        width: 400,
        height: 400,
        frame: false,
        alwaysOnTop: true,
        center: true,
        show: true
    });
    splashWindow.loadFile(path.join(__dirname, 'splash.html'));

    const mainWindow = new BrowserWindow({
        autoHideMenuBar: true,
        width: 800,
        height: 600,
        show: false
    });
    mainWindow.loadURL('https://college-management-system-786.herokuapp.com/');
    mainWindow.once('ready-to-show', () => {
        splashWindow.destroy()
        mainWindow.show();
    });

    mainWindow.webContents.on('did-fail-load', () => { 
        mainWindow.loadFile(path.join(__dirname, 'error.html'));
    });
});