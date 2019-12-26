import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OrderFormComponent } from './order-form/order-form.component';
import {OrderComponent} from './order.component';
import { ApiService } from '../api.service';
import {Routes, RouterModule} from '@angular/router';
import {ReactiveFormsModule, FormsModule} from '@angular/forms'

const routes: Routes = [
  {path: 'order-form', component: OrderComponent}
];

@NgModule({
  declarations: [
    OrderFormComponent,
    OrderComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(routes),
    FormsModule,
    ReactiveFormsModule
  ],
  exports: [
    RouterModule
  ],
  providers:[
    ApiService
  ]
})
export class OrderModule { }
