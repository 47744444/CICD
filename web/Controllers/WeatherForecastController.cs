using Microsoft.AspNetCore.Mvc;
using System;

namespace WebApplication1.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class WeatherForecastController : ControllerBase
    {
        [HttpGet(Name = "GetWeatherForecast")]
        public IActionResult Get()
        {
            return Ok("Hello");
        }
    }
}
