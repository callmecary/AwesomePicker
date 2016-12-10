using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Net;
using System.Threading.Tasks;
using AwesomePicker.Models;

namespace AwesomePicker.Controllers
{
    public class StockController : Controller
    {
        //public IActionResult Index()
        //{
        //    return View();
        //}
        [ActionName("Index")]
        public async Task<ActionResult> IndexAsync()
        {
            var stocks = await DocumentDBRepository<Stock>.GetStockedPickedAsync(d=>1==1);
            return View(stocks);
        }

    }
}