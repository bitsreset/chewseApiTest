from django.shortcuts import render
from .models import Item,Order,PortionDetails
from .forms import OrderForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
import copy
from .utils import allocation_portions,distribute
import ast

def order_detail(request, pk):
    order_post = get_object_or_404(Order, pk=pk)
    portion_details = PortionDetails.objects.filter(orderID=pk).values('itemID','item','allocated_portions')
    allocation_list = [each_list for each_list in portion_details] if portion_details else None
    return render(request, 'api_app/order_detail.html', {'post': order_post,'allocation_list':allocation_list})

# Create your views here.
def index(request):
    items = Item.objects.all()
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_dict = request.POST.get('order_dict')
            order.save()

            #Code for Portion Allocation
            test_dict = ast.literal_eval(order.order_dict)
            portions = request.POST.get('portions')
            allocated_dict = distribute(test_dict, portions )
            #print(allocated_dict)

            if allocated_dict:
                record_list = list()

                for key in set(test_dict.keys()) & set(allocated_dict.keys()):
                    each_record = dict()
                    each_record['orderID'] = order.pk
                    each_record['itemID'] = key
                    each_record['item'] = Item.objects.get(id=key)
                    each_record['ratio'] = test_dict[key]
                    each_record['allocated_portions'] = test_dict[key]

                    record_list.append(each_record)


                #create/Save new record
                #print(record_list)
                for each_record_dict in record_list:
                    #print(each_record_dict)
                    each_record_object = PortionDetails(**each_record_dict)
                    each_record_object.save()
            else:
                pass

            #redirect
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()

    return render(request,'api_app/index.html', {'items':items,'form': form})