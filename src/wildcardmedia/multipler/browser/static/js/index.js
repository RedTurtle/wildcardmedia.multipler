import React from 'react';
import ReactDOM from 'react-dom';
import VideoPlayer from './VideoPlayer';

const root = document.getElementById('multipler-video');

if (root) {
  const videoData = root.getAttribute('data-video-data');
  ReactDOM.render(<VideoPlayer {...JSON.parse(videoData)} />, root);
}
