from django.shortcuts import render


# Create your views here.
from django.shortcuts import HttpResponse
def index(request):
	return render(request,'index.html')
	#return HttpResponse("India is great country")

def data(request):
	details = [
          {'Name':'Mohan','Aadhar_no':'8888 5555 4444','Contact':'9988554433','Address':'456/A, Ganga Nagar , Delhi'},
          {'Name':'Raj','Aadhar_no':'4525 7845 1258','Contact':'2541687901','Address':'789, Green Avenue, Mumbai'},
          {'Name':'Ananya Desai','Aadhar_no':'8989 5555 4646','Contact':'8888521525','Address':'101, Silver Heights,Ahmedabad'},
          {'Name':'Aaliya Thakkar','Aadhar_no':'5979 5486 1259','Contact':'9485621780','Address':'105,Shakti Society ,Ahmedabad'},
          {'Name':'Mahek Sharma','Aadhar_no':'8745 8952 4444','Contact':'9000999014','Address':'101, 22, Lotus Lane,Delhi'},
          {'Name':'Priya Verma','Aadhar_no':'7979 8546 2145','Contact':'1234567890','Address':'101, 33, Himalaya Road,Mumbai'}
	]
	return render(request,'data.html' , {'details' : details})	





from django.shortcuts import render, HttpResponseRedirect

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        aadhar_no = request.POST.get('aadhar_no')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        
        # Fetch existing session data if any, or initialize an empty list
        registration_data_list = request.session.get('registration_data_list', [])
        
        # Append new form data to the list
        registration_data_list.append({
            'name': name,
            'aadhar_no': aadhar_no,
            'contact': contact,
            'address': address
        })
        
        # Store the updated list back into the session
        request.session['registration_data_list'] = registration_data_list
        
        return HttpResponseRedirect('show')
    else:
        return render(request, 'registration.html')

def show(request):
    # Fetch the session data list
    registration_data_list = request.session.get('registration_data_list', [])
    
    return render(request, 'show.html', {'registration_data_list': registration_data_list})



# this is other way :
'''from django.http import HttpResponseRedirect

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        aadhar_no = request.POST.get('aadhar_no')
        contact = request.POST.get('contact')
        address = request.POST.get('Address')
        request.session['name'] = name
        request.session['aadhar_no'] = aadhar_no
        request.session['contact'] = contact
        request.session['address'] = address
        return HttpResponseRedirect('show')
    else:
        return render(request, 'registration.html')

def show(request):
    name = request.session.get('name')
    aadhar_no = request.session.get('aadhar_no')
    contact = request.session.get('contact')
    address = request.session.get('address')
    return render(request, 'show.html', {'name': name, 'aadhar_no' : aadhar_no, 'contact' : contact, 'address':address})


'''