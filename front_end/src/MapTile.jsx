import React from 'React';
import CSSModules from 'react-css-modules'
import styles from './css/MapTile.css'

class MapTile extends React.Component{
  constructor() {
    super();
    this.state = {
      terrain: 'none'
    };
  }

  render() {
    return(
      <div styleName='hexagon'/>
    )
  }
}
export default CSSModules(MapTile, styles);
