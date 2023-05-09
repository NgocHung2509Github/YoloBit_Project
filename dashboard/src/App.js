import React, { useState } from 'react';
import { Switch, FormControlLabel, Card, CardHeader, CardContent, Typography } from '@mui/material';
import { Dashboard } from '@mui/icons-material';
import TemperatureGauge from './components/TemperatureGauge';
import MySwitch from './components/MySwitch';
import './App.css';

function App() {

  return (
    <>
    <div className="container-fluid h-100">  
      <div className="row sidebar">
        <div className="col-md-2 p-4">
          <div className="d-flex align-items-center mb-4">
              <Dashboard sx={{mr: 1, fontSize: 36, color: '#fff'}}/>
              <Typography variant="h5" sx={{color: '#fff'}}>Dashboard</Typography>
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col-md-2 p-4"></div>
        <div className="col-md-4 pt-5 ps-5 pe-5">
          <Card sx={{mb: 2}}>
              <CardHeader title="Fan" sx={{justifyContent: 'center'}}/>
              <CardContent sx={{display: 'flex', justifyContent: 'center'}}>
                <MySwitch />
              </CardContent>
            </Card>
            <Card sx={{mb: 2}}>
              <CardHeader title="Light" sx={{justifyContent: 'center'}}/>
              <CardContent sx={{display: 'flex', justifyContent: 'center'}}>
                <MySwitch />
              </CardContent>
            </Card>
            <Card sx={{mb: 4}}>
              <CardHeader title="Temperature" sx={{justifyContent: 'center'}}/>
              <CardContent sx={{display: 'flex', justifyContent: 'center'}}>
                <TemperatureGauge temperature={40} />
              </CardContent>
            </Card>
        </div>
        <div className="col-md-6 pt-5 ps-5 pe-5">
          <Card sx={{mb: 2}}>
            <CardHeader title="Camera" sx={{color: 'black'}}/>
            <CardContent sx={{display: 'block', justifyContent: 'center'}}>
              [Add your picture here]
            </CardContent>
          </Card>
          <Card sx={{mb: 2}}>
            <CardHeader title="Status" sx={{color: 'black'}}/>
            <CardContent sx={{height: '100%'}}>
              <div className="d-flex flex-column justify-content-center align-items-center h-100">
                <Typography variant="h6" component="span">Owner</Typography>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardHeader title="Text Log" sx={{backgroundColor: 'gray', color: 'white'}}/>
            <CardContent sx={{height: '100%'}}>
              <Typography variant="body1" sx={{height: '100%', display: 'flex', alignItems: 'center'}}>
                [Add your text log here]
              </Typography>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
    </>
  );
}

export default App;
