import { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';


/*
 *
 *  add artist
 *  update artist
 *
 *  add release and tracks to existing artist
 *  add release and tracks to new artist
 *
 *  update release
 *  update tracks
 *
 */
function ArtistSelect({ artists }) {
    
    return (
        <div className="artist-select">
            <div>
                <label>Select an Artist: </label>
                <select>
                    <option key={-1} value="">------------</option>
                    {
                        artists.map(artist => 
                            <option
                                key={artist.id}
                                value={artist.id}>
                            {artist.name}
                            </option>
                        )
                    }
                </select>
            </div>
            <div>
                or
            </div>
            <div>
                add a new one <input type="text" placeholder="new artist name"/>
            </div>

        </div>
    );
}
function App() {

    const [artists, setArtists] = useState([]); 

    useEffect(() => {

        async function getArtists() {
            try {
                const { data } = await axios.get('http://localhost:5000/api/artists');
                return data.artists;
            } catch(e) {
                console.log(e);
            }
        }

        getArtists().then(setArtists);
      
    }, []);

    return (
        <div className="App">
            <ArtistSelect artists={artists} />
        </div>
    );
}

export default App;
