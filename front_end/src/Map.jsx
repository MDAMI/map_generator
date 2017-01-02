import React from 'react';
import CSSModules from 'react-css-modules';
import styles from './css/Map.css'
import MapTile from './MapTile'

class Map extends React.Component {
  constructor() {
    super();
    this.state = {
      mapArray: [
        ['none', 'none', 'none', 'none'],
        ['none', 'none', 'none', 'none'],
        ['none', 'none', 'none', 'none'],
        ['none', 'none', 'none', 'none'],]
    };
  }

  render() {
    var mapRender = this.state.mapArray.map(
      function(tileArray){
        var tiles = tileArray.map(
          tile => <MapTile terrain={tile}/>
        )
        return <div>{tiles}</div>
      }
    );
    return (
      <MapTile/>
    );
  }
}
export default CSSModules(Map, styles);
