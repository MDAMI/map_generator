import React from 'react';
import ReactDOM from 'react-dom';
import Map from './Map';

document.addEventListener('DOMContentLoaded', function() {
  ReactDOM.render(
    React.createElement(Map),
    document.getElementById('mount')
  );
});
