import { useState, useEffect } from 'react';
import Matches from './matches';
import useFetch from './useFetch';

const Match = () => {
    const {data, isLoading, error} = useFetch('http://localhost:8000/matches');
    return (
        <div className="match-container">
            {error && <div>{error}</div>}
            {isLoading && <div color="white">Loading...</div>}
            {data && <Matches matches={data} />}
        </div>
    );
}
 
export default Match;