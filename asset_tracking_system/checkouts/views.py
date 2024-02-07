
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CheckoutForm
from .models import Checkout
from devices.models import Device, DeviceLog



def checkout_list(request):
    checkouts = Checkout.objects.all()
    return render(request, 'checkouts/checkout_list.html', {'checkouts': checkouts})

def checkout_detail(request, checkout_id):
    checkout = Checkout.objects.get(pk=checkout_id)
    return render(request, 'checkouts/checkout_detail.html', {'checkout': checkout})

def checkout_create(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            checkout = form.save()
            device = checkout.device
            DeviceLog.objects.create(
                device=device,
                event_type='Checked out',
                condition=device.condition,
            )
            messages.success(request, 'Checkout created successfully.')
            return redirect('checkout_list')
    else:
        form = CheckoutForm()
    return render(request, 'checkouts/checkout_create.html', {'form': form})

def checkout_update(request, checkout_id):
    checkout = Checkout.objects.get(pk=checkout_id)
    if request.method == 'POST':
        form = CheckoutForm(request.POST, instance=checkout)
        if form.is_valid():
            updated_checkout = form.save()
            device = updated_checkout.device
            DeviceLog.objects.create(
                device=device,
                event_type='Returned',
                condition=device.condition,
            )
            messages.success(request, 'Checkout updated successfully.')
            return redirect('checkout_list')
    else:
        form = CheckoutForm(instance=checkout)
    return render(request, 'checkouts/checkout_update.html', {'form': form})
