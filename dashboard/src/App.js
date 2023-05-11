import React, { useState, useEffect } from 'react';
import { FormControlLabel, Card, CardHeader, CardContent, Typography } from '@mui/material';
import { Dashboard } from '@mui/icons-material';
import TemperatureGauge from './components/TemperatureGauge';
import MySwitch from './components/MySwitch';
import './App.css';

function App() {

  const [fanSwitch, setFanSwitch] = useState(false);
  const [lightSwitch, setLightSwitch] = useState(false);
  const [temperature, setTemperature] = useState(0);
  const [status, setStatus] = useState("Block");
  const [name, setName] = useState("None");

  const handleFanSwitchChange = (event) => {
    setFanSwitch(event.target.checked);

    fetch('/fanswitch/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        fan_switch: event.target.checked ? 1 : 0
      })
    });
  };

  const handleLightSwitchChange = (event) => {
    setLightSwitch(event.target.checked);

    fetch('/lightswitch/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        light_switch: event.target.checked ? 1 : 0
      })
    });
  };

  useEffect(() => {
    const intervalId = setInterval(() => {
      fetch('/temperature/')
        .then(response => response.json())
        .then(data => {
          setTemperature(data.temperature);
        })
        .catch(error => console.error(error));

      fetch('/status/')
        .then(response => response.json())
        .then(data => {
          setStatus(data.detectstatus);
        })
        .catch(error => console.error(error));

      fetch('/name/')
        .then(response => response.json())
        .then(data => {
          setName(data.detectname);
        })
        .catch(error => console.error(error));

    }, 5000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <>
    <div className="container-fluid h-100">  
      <div className="row sidebar">
        <div className="col-md-2 p-4">
          <div className="d-flex align-items-center mb-4">
              <Dashboard sx={{mr: 1, fontSize: 36, color: '#fff'}}/>
              <Typography variant="h5" sx={{mr: 1, color: '#fff'}}>Dashboard</Typography>
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col-md-2 p-4"></div>
        <div className="col-md-4 pt-5 ps-5 pe-5">
          <Card sx={{mb: 2, backgroundColor: '#3c4141'}}>
              <CardHeader title="Fan" sx={{color: 'white', justifyContent: 'center'}}/>
              <CardContent sx={{display: 'flex', justifyContent: 'center'}}>
                <FormControlLabel
                  value = "fan_switch"
                  control = {<MySwitch id = "fan-switch" checked={fanSwitch} onChange={handleFanSwitchChange} />}
                  label=""
                  labelPlacement="bottom"
                />
              </CardContent>
            </Card>
            <Card sx={{mb: 2, backgroundColor: '#3c4141'}}>
              <CardHeader title="Light" sx={{color: 'white', justifyContent: 'center'}}/>
              <CardContent sx={{display: 'flex', justifyContent: 'center'}}>
                <FormControlLabel
                  value = "light_switch"
                  control = {<MySwitch id = "light-switch" checked={lightSwitch} onChange={handleLightSwitchChange} />}
                  label=""
                  labelPlacement="bottom"
                />
              </CardContent>
            </Card>
            <Card sx={{mb: 3, backgroundColor: '#3c4141'}}>
              <CardHeader title="Temperature" sx={{color: 'white', justifyContent: 'center'}}/>
              <CardContent sx={{color: 'white', display: 'flex', justifyContent: 'center'}}>
                <TemperatureGauge temperature={temperature} />
              </CardContent>
            </Card>
        </div>
        <div className="col-md-6 pt-5 ps-5 pe-5">
          <Card sx={{mb: 2, backgroundColor: '#3c4141'}}>
            <CardHeader title="Status" sx={{color: 'white'}}/>
            <CardContent sx={{height: '100%'}}>
              <div className="d-flex flex-column justify-content-center align-items-center h-100 p-4">
                <strong>
                  <Typography variant="h3" component="span" className={status === 'Allow' ? 'green-text' : 'red-text'}>{'>>' + status + '<<'}</Typography>
                </strong>
              </div>
            </CardContent>
          </Card>
          <Card sx={{mb: 4, backgroundColor: '#3c4141'}}>
            <CardHeader title="Name" sx={{color: 'white'}}/>
              <CardContent sx={{height: '100%'}}>
                <div className="d-flex flex-column justify-content-center align-items-center h-100 p-4">
                  <strong>
                    <Typography variant="h3" component="span" sx={{color: 'white'}}>{name}</Typography>
                  </strong>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
    </>
  );
}

export default App;
