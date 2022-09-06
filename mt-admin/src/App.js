import logo from './logo.svg';
import './App.css';


function ArtistSelect(props) {
    
    return (
        <div className="artist-select">
            <select>
                <option value="">------------</option>
                {
                    props.artists.map(artist => <option value={artist.id}>{artist.name}</option>)
                }
            </select>
        </div>
    );
}

function App() {

    const artists = [{
        name: "Al's Magic",
        id: 1,
    },
    {
        name: 'floodreed',
        id: 2
    }];

    return (
        <div className="App">
            <ArtistSelect artists={artists} />
        </div>
    );
}

export default App;
