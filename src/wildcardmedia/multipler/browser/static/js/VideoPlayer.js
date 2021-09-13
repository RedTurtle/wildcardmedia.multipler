import React from 'react';
import PropTypes from 'prop-types';
import VideoJS from './VideoJS'; // point to where the functional component is stored

const VideoPlayer = ({ videoUrl, posterUrl, language }) => {
  const playerRef = React.useRef(null);
  const videoJsOptions = {
    // lookup the options in the docs for more options
    autoplay: false,
    controls: true,
    responsive: true,
    fluid: true,
    playbackRates: [0.5, 1, 1.25, 1.5, 1.75, 2],
    language: language,
    poster: posterUrl,
    sources: [
      {
        src: videoUrl,
      },
    ],
  };

  const handlePlayerReady = player => {
    playerRef.current = player;
  };

  return <VideoJS options={videoJsOptions} onReady={handlePlayerReady} />;
};

VideoPlayer.propTypes = {
  videoUrl: PropTypes.string,
  posterUrl: PropTypes.string,
  language: PropTypes.string,
};

export default VideoPlayer;
