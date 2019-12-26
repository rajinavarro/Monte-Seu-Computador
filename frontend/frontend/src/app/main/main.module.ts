import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainComponent } from './main.component';
import {Routes, RouterModule} from '@angular/router';
import { OrderListComponent } from './order-list/order-list.component';
import { OrderDetailsComponent } from './order-details/order-details.component';
import { ApiService } from '../api.service';
import {ProductListComponent} from './product-list/product-list.component';


const routes: Routes = [
  {path: 'orders', component: MainComponent}
];


@NgModule({
  declarations: [
    MainComponent,
    OrderListComponent,
    OrderDetailsComponent,
    ProductListComponent,
    

  ],
  imports: [
    CommonModule,
    RouterModule.forChild(routes)
  ],
  exports: [
    RouterModule
  ],
  providers: [
    ApiService
  ]
})
export class MainModule { }
