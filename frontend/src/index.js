// index.js - ./frontend/src/index.js
// This is the main entry point for the React frontend application.
// It imports the App component and renders it to the DOM.

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render( <
    React.StrictMode >
    <
    App / >
    <
    /React.StrictMode>,
    document.getElementById('root')
);