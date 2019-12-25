import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { OrderListComponent } from './order-list/order-list.component';
import { OrderService } from './order.service';

@NgModule({
  declarations: [
    AppComponent,
    OrderListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [OrderService],
  bootstrap: [AppComponent]
})
export class AppModule { }
