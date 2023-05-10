import { CircularProgress, Typography } from '@mui/material';

function CircularProgressWithLabel(props) {
  const { value, temperature } = props;

  return (
    <div
      style={{
        position: 'relative',
        display: 'inline-block',
      }}
    >
      <CircularProgress variant="determinate" value={value} {...props} sx={{ color: '#0E8388', thickness: 5 }} />
      <Typography
        variant="h5"
        component="div"
        style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)' }}
      >
        {temperature}°C
      </Typography>
    </div>
  );
}

function TemperatureGauge({ temperature }) {
  const maxTemperature = 60;
  const threshold = 50;

  // Convert Celsius to a 0 to 60 scale
  const value = (temperature / maxTemperature) * 100;

  // Determine color based on threshold
  const color = value >= threshold ? 'error' : 'primary';

  return (
    <CircularProgressWithLabel value={value} temperature={temperature} color={color} size={100} />
  );
}



export default TemperatureGauge;