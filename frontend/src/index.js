import React from 'react';
import ReactDOM from 'react-dom';
import { Button, ButtonGroup } from 'reactstrap';

import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css'

const styles = {
  "pop-anime":     { textAlign: "center", color: '#ff972a' },
  "nico-vocaloid": { textAlign: "center", color: '#09c8d4' },
  "touhou":        { textAlign: "center", color: '#ba60ff' },
  "game-variety":  { textAlign: "center", color: '#42de6a' },
  "maimai":        { textAlign: "center", color: '#f74949' }
};

function key_translate(ss) {
  switch (ss) {
    case "流行＆动漫": return "pop-anime";
    case "niconico＆VOCALOID": return "nico-vocaloid";
    case "东方Project": return "touhou";
    case "综艺节目": return "game-variety";
    case "原创乐曲": return "maimai";
    default:
      return undefined;
  }
}

function DisplayResult(props) {
  const style_c = styles[key_translate(props.Category)];
  return (
    <div className='py-3'>
      <div name='Category' style={style_c}><h5>{props.Category}</h5></div>
      <div name='MusicName' style={{textAlign: "center",}}><h3>{props.MusicName}</h3></div>
      <div name='Difficulty' style={{textAlign: "center",}}><h5>{props.Difficulty}&nbsp;{props.Stars}</h5></div>
    </div>
  );
}

class Navibar extends React.Component {
  render() {
    return (
        <nav className='navbar navbar-expand-sm navbar-dark bg-dark'>
          <a className='navbar-brand' href='#'>今天打什么</a>
        </nav>
    );
  }
}

class MaimaiSelector extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      Category: [],
      Difficulty: 'Any',
      starsLowerBound: '1',
      starsUpperBound: '14',
      starsList: ['1', '2', '3', '4', '5', '6', '7', '7+', '8', '8+', '9', '9+', '10', '10+', '11', '11+', '12', '12+', '13', '13+', '14'],

      returnCategory: [],
      returnDifficulty: '',
      returnMusicName: '',
      returnStar: '',
    }

    this.handleCategoryChange = this.handleCategoryChange.bind(this);
    this.handleDifficultyChange = this.handleDifficultyChange.bind(this);
    this.handleStarsLowerBoundChange = this.handleStarsLowerBoundChange.bind(this);
    this.handleStarsUpperBoundChange = this.handleStarsUpperBoundChange.bind(this);

    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    let params = {
      'Category': this.state.Category,
      'Difficulty': this.state.Difficulty,
      'starsLowerBound': this.state.starsLowerBound,
      'starsUpperBound': this.state.starsUpperBound,
    };

    fetch('/data',
      {
        method: 'POST',
        body: JSON.stringify(params),
        headers: {
          'content-type': 'application/json'
        }
      }).then((response) => (response.json()))
      .then((data) => {
        console.log(data);
        this.setState({
          returnCategory: data.Category,
          returnDifficulty: data.Difficulty,
          returnMusicName: data.MusicName,
          returnStar: data.Stars,
        });
      });

    event.preventDefault();
  }

  handleCategoryChange(selected) {
    let category_selected = this.state.Category.slice();
    let index = category_selected.indexOf(selected);

    if (index < 0) {
      category_selected.push(selected);
    } else {
      category_selected.splice(index, 1);
    }

    if (selected === "RESET") {
      category_selected.length = 0;
    }

    this.setState({
      Category: category_selected,
    });
  }

  handleDifficultyChange(event) {
    this.setState({
      Difficulty: event.target.value,
    })
  }

  handleStarsLowerBoundChange(event) {
    this.setState({
      starsLowerBound: event.target.value,
    })
  }

  handleStarsUpperBoundChange(event) {
    this.setState({
      starsUpperBound: event.target.value,
    })
  }

  render() {
    const starsList = this.state.starsList.slice();
    const allStarOptions = starsList.map(
      (stars) => <option key={stars} value={stars}>{stars}</option>
    );

    return (
      <div className='container py-3'>
        <div className="result">
          { this.state.returnMusicName === "" ? null : <DisplayResult
            Category={this.state.returnCategory}
            MusicName={this.state.returnMusicName}
            Difficulty={this.state.returnDifficulty}
            Stars={this.state.returnStar}
          />
          }

        </div>
        <div className="Select">
          <form onSubmit={this.handleSubmit}>
            <div className="row py-1">
              <div className="col-sm-1" style={{ paddingTop: "0.4em", whiteSpace: "nowrap" }}>流派</div>
              <ButtonGroup className="col">
                <Button outline color='pop-anime' onClick={() => this.handleCategoryChange('流行＆动漫')} active={this.state.Category.includes('流行＆动漫')}>流行＆动漫</Button>
                <Button outline color='nico-vocaloid' onClick={() => this.handleCategoryChange('niconico＆VOCALOID')} active={this.state.Category.includes('niconico＆VOCALOID')}>nico<wbr />nico<wbr />＆<wbr />VOCA<wbr />LOID</Button>
                <Button outline color='touhou' onClick={() => this.handleCategoryChange('东方Project')} active={this.state.Category.includes('东方Project')}>东方Project</Button>
                <Button outline color='game-variety' onClick={() => this.handleCategoryChange('综艺节目')} active={this.state.Category.includes('综艺节目')}>综艺节目</Button>
                <Button outline color='maimai' onClick={() => this.handleCategoryChange('原创乐曲')} active={this.state.Category.includes('原创乐曲')}>原创乐曲</Button>
                <Button outline color='secondary' onClick={() => this.handleCategoryChange('RESET')}>清空</Button>
              </ButtonGroup>
            </div>
            <div className="row py-1">
              <div className="col-sm-1" style={{ paddingTop: "0.4em", whiteSpace: "nowrap" }}>难度</div>
              <div className="col-sm-5">
                <select className='btn btn-secondary dropdown-toggle d-block' name='Difficulty' value={this.state.Difficulty} onChange={this.handleDifficultyChange}>
                  <option value='Any'>不限</option>
                  <option value='Master+Re' style={{ backgroundColor: "white", color: "#c948e7", fontWeight: "bold" }}>Master＆Re:Master</option>
                  <option value='Re:Master' style={{ backgroundColor: "white", color: "#c958e7", fontWeight: "bold" }}>Re:Master</option>
                  <option value='Master' style={{ backgroundColor: "#CC99FF", color: "black", fontWeight: "" }}>Master</option>
                  <option value='Expert' style={{ backgroundColor: "#FFBBDB", color: "black", fontWeight: "" }}>Expert</option>
                  <option value='Advanced' style={{ backgroundColor: "#FFD17D", color: "black", fontWeight: "" }}>Advanced</option>
                  <option value='Basic' style={{ backgroundColor: "#BBFFAC", color: "black", fontWeight: "" }}>Basic</option>
                </select>
              </div>
              <div className="col-sm-1" style={{ paddingTop: "0.4em", whiteSpace: "nowrap" }}>等级带</div>
              <div className="col-sm-5" style={{ whiteSpace: "nowrap" }}>
                <select className='btn btn-light dropdown-toggle' name='starsLowerBound' value={this.state.starsLowerBound} onChange={this.handleStarsLowerBoundChange}>
                  {allStarOptions}
                </select>
                ～
                <select className='btn btn-light dropdown-toggle' name='starsUpperBound' value={this.state.starsUpperBound} onChange={this.handleStarsUpperBoundChange}>
                  {allStarOptions}
                </select>
              </div>
            </div>
            <div className="col py-3" style={{ textAlign: "center" }}>
              <Button color='primary' type="submit" className='col-6'>提交</Button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

ReactDOM.render(
    <Navibar />,
    document.getElementById('navbar')
)

ReactDOM.render(
  <MaimaiSelector />,
  document.getElementById('root')
);
