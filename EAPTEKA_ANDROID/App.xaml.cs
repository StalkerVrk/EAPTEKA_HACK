using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace EAPTEKA_ANDROID
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent(); 

            MainPage = new MainPage(); //Задаём страницу которая показывается пользователю
        }

        protected override void OnStart()
        {
        }

        protected override void OnSleep()
        {
        }

        protected override void OnResume()
        {
        }
    }
}
