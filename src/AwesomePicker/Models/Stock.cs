using Newtonsoft.Json;
using System;
using System.ComponentModel.DataAnnotations;

namespace AwesomePicker.Models
{
    public class Stock
    {
        [JsonProperty(PropertyName = "id")]
        public string Id { get; set; }

        [DisplayFormat(DataFormatString = "{0:yyyy-MM-dd}", ApplyFormatInEditMode = true)]
        [JsonProperty(PropertyName = "asofDate")]
        public DateTime AsofDate { get; set; }

        [JsonProperty(PropertyName = "symbol")]
        public string Symbol { get; set; }

        [JsonProperty(PropertyName = "open")]
        public double Open { get; set; }

        [JsonProperty(PropertyName = "pre_close")]
        public double PreviousClose { get; set; }

        [JsonProperty(PropertyName ="moving")]
        public double Moving { get; set; }
        
        [JsonProperty(PropertyName ="past90daymoving")]
        public double Past90dayMoving { get; set; }

        [JsonProperty(PropertyName ="action")]
        public string Action { get; set; }
    }
}
