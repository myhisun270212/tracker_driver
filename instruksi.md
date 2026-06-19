Cara memaksa lebih akurat
navigator.geolocation.getCurrentPosition(
  success,
  error,
  {
    enableHighAccuracy: true,
    timeout: 30000,
    maximumAge: 0
  }
);