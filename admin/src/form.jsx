import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';

import axios from './axios';

const Form = () => {
  const [formData, setFormData] = useState({
    title: '',
    link: '',
    image: null,
  });

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: files ? files[0] : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = new FormData();
    data.append('title', formData.title);
    data.append('link', formData.link);
    if (formData.image) {
      data.append('image', formData.image);
    }

    try {
      const response = await axios.post('/submit', data);

      if (response.status === 200) {
        console.log('Form submitted successfully');
        setFormData({ title: '', link: '', image: null });
      } else {
        console.error('Failed to submit the form');
      }
    } catch (error) {
      console.error('Error submitting the form:', error);
    }
  };

  return (
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
        backgroundColor: '#f5f5f5', // Light background for contrast
      }}
    >
      <Paper
        elevation={4}
        sx={{
          p: 4, // Padding inside the form
          width: '400px', // Adjust the width as needed
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          borderRadius: 2, // Rounded corners
          boxShadow: '0px 4px 20px rgba(0, 0, 0, 0.1)', // Subtle shadow effect
        }}
      >
        <Box
          component="form"
          sx={{
            '& .MuiTextField-root': { m: 2, width: '100%' }, // Larger inputs
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            width: '100%', // Make inputs take full width
          }}
          noValidate
          autoComplete="off"
          onSubmit={handleSubmit}
        >
          <TextField
            label="Title"
            variant="outlined"
            name="title"
            value={formData.title}
            onChange={handleChange}
            required
          />
          <TextField
            label="Link"
            variant="outlined"
            name="link"
            value={formData.link}
            onChange={handleChange}
            required
          />
          <TextField
            type="file"
            variant="outlined"
            name="image"
            onChange={handleChange}
          />
          <Button variant="contained" color="primary" type="submit" sx={{ mt: 3 }}>
            Submit
          </Button>
        </Box>
      </Paper>
    </Box>
  );
};

export default Form;
