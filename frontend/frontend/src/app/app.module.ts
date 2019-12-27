import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainModule } from './main/main.module';
import { ProductsModule} from './products/products.module';
import { HttpClientModule } from '@angular/common/http';
import { OrderModule } from './order/order.module';

const routes: Routes = [
  {path: '', pathMatch: 'full', redirectTo:'orders'},
  {path: 'products', pathMatch: 'full', redirectTo:'products'},
  {path: 'order-form', pathMatch: 'full', redirectTo: 'order-form'}
];

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MainModule,
    ProductsModule,
    RouterModule.forRoot(routes),
    HttpClientModule,
    OrderModule
  ],
  exports: [
    RouterModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
