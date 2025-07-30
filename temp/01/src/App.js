import React, { useState } from 'react';
import { Container, TextField, List, ListItem, ListItemText, Typography } from '@mui/material';
import { styled } from '@mui/system';

// Sample data for movies
const moviesData = [
  { title: 'Inception', genre: 'Sci-Fi', year: 2010 },
  { title: 'The Dark Knight', genre: 'Action', year: 2008 },
  { title: 'Interstellar', genre: 'Sci-Fi', year: 2014 },
  { title: 'The Prestige', genre: 'Thriller', year: 2006 },
  { title: 'Memento', genre: 'Mystery', year: 2000 }
];

// Styled components using Material-UI
const ContainerStyled = styled(Container)({
  marginTop: '20px',
});

const TextFieldStyled = styled(TextField)({
  marginBottom: '20px',
});

const ListItemStyled = styled(ListItem)({
  borderBottom: '1px solid #ccc',
});

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [movies, setMovies] = useState(moviesData);

  // Function to handle search input
  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
    const filteredMovies = moviesData.filter((movie) =>
      movie.title.toLowerCase().includes(event.target.value.toLowerCase())
    );
    setMovies(filteredMovies);
  };

  return (
    <ContainerStyled>
      <Typography variant="h4" gutterBottom>Movie List</Typography>
      <TextFieldStyled
        label="Search movies..."
        variant="outlined"
        fullWidth
        value={searchTerm}
        onChange={handleSearch}
      />
      <List>
        {movies.map((movie, index) => (
          <ListItemStyled key={index}>
            <ListItemText
              primary={<Typography variant="h6">{movie.title}</Typography>}
              secondary={
                <>
                  <Typography variant="body2">Genre: {movie.genre}</Typography>
                  <Typography variant="body2">Year: {movie.year}</Typography>
                </>
              }
            />
          </ListItemStyled>
        ))}
      </List>
    </ContainerStyled>
  );
};

export default App;
