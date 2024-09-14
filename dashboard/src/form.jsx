import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import axios from './axios';

const Form = () => {
  const [formData, setFormData] = useState({
    title: '',
    link: '',
    image: '',
    date: '',
    time: '',
    tags: '',
    publisher: '',
    field: 'news'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const data = new FormData();
    Object.keys(formData).forEach((key) => {
      if (formData[key]) {
        data.append(key, formData[key]);
      }
    });
    
    try {
      const response = await axios.post('/submit', data, {
       headers: {
          "Content-Type": "multipart/form-data", // Correct content type for FormData
        }, 
      });

      if (response.status === 200) {
        console.log('Form submitted successfully');
        setFormData({
          title: '',
          link: '',
          image: '',
          date: '',
          time: '',
          tags: '',
          publisher: '',
          field: 'news' // Reset field to default value
        });
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
        backgroundColor: '#f5f5f5',
      }}
    >
      <Paper
        elevation={4}
        sx={{
          p: 4,
          width: '400px',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          borderRadius: 2,
          boxShadow: '0px 4px 20px rgba(0, 0, 0, 0.1)',
        }}
      >
        <Box
          component="form"
          sx={{
            '& .MuiTextField-root': { m: 2, width: '100%' },
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            width: '100%',
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
            label="Image URL"
            variant="outlined"
            name="image"
            value={formData.image}
            onChange={handleChange}
          />
          <TextField
            label="Date"
            variant="outlined"
            name="date"
            value={formData.date}
            onChange={handleChange}
          />
          <TextField
            label="Time"
            variant="outlined"
            name="time"
            value={formData.time}
            onChange={handleChange}
          />
          <TextField
            label="Tags (comma separated)"
            variant="outlined"
            name="tags"
            value={formData.tags}
            onChange={handleChange}
          />
          <TextField
            label="Publisher"
            variant="outlined"
            name="publisher"
            value={formData.publisher}
            onChange={handleChange}
          />
          <Select
            label="Field"
            name="field"
            value={formData.field}
            onChange={handleChange}
            variant="outlined"
            sx={{ m: 2, width: '100%' }}
          >
            <MenuItem value="news">News</MenuItem>
            <MenuItem value="events">Events</MenuItem>
            {/* Add more options as needed */}
          </Select>
          <Button variant="contained" color="primary" type="submit" sx={{ mt: 3 }}>
            Submit
          </Button>
        </Box>
      </Paper>
    </Box>
  );
};

export default Form;
