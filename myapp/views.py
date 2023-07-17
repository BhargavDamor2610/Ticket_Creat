from django.shortcuts import render
from django.shortcuts import redirect, render
from myapp.models import USER,DEPARTMENT
from django.db.models import Q
from django.core import mail

# Create your views here.

def Home(request):
    alluser=USER.objects.all()
    return render (request,"alluser.html",{'alluser':alluser})

def login(request):
    if 'id' in request.session:
        return redirect('Home')
    
    else:
        if request.method == "POST":
            username = request.POST.get('email')
            password = request.POST.get('password')
           
            
            try:
                
               user = USER.objects.get(Q(Email=username) | Q(Mobile_Number=username)) 
            except:
                e_msg="email id is not registered"
                return render(request, 'login.html',{"e_msg":e_msg})
           
            if username == user.Email or username == user.Mobile_Number:
                if password == user.Password:
                    if user.Role == "user":
                        request.session['id'] = user.id
                        return render(request,"index.html")
                    else:           
                        request.session['id'] = user.id
                        return redirect('Home')
                else:
                    e_msg="password is invalid"
                    return render(request,'login.html',{"e_msg":e_msg})
            else:
                e_msg="Username is invalid"
                return render(request, 'Login.html',{"e_msg":e_msg})
                
        else:
            return render(request,"login.html")
 
def logout(request):
    del request.session['id']
    return redirect('login')

def User(request):
    if request.method=="POST":
        if request.method=="POST":
            Name = request.POST.get('name')
            Email = request.POST.get('email')
            mobile_Number = request.POST.get('Mob_num')
            Role = request.POST.get('Role')
            Department = request.POST.get('Department')
            Password=request.POST.get('Password')

            did=DEPARTMENT.objects.get(Name=Department)

            USER.objects.create(
                Name=Name,
                Email=Email,
                Mobile_Number=mobile_Number,
                Password=Password,
                Role=Role,
                Department=did
                
            )
            return redirect('Home')
        else:
            return render(request,"userform.html")
    else:
        return render(request,"login.html")

def add_user(request):
    AllDepartment=DEPARTMENT.objects.all()
    return render(request,"userform.html",{'AllDepartment':AllDepartment})

def department(request):
    AllDepartment=DEPARTMENT.objects.all()
    return render(request,"department.html",{'AllDepartment':AllDepartment})

def add_department(request):
    if request.method=="POST":
        Name = request.POST.get('Department_name')
        Description = request.POST.get('description')
        
        DEPARTMENT.objects.create(
            Name=Name,
            Description=Description,
           
        )
        return redirect('department')
        
    else:
        return redirect('department')
    

def department_edit(request,pk):
    if 'id'  in request.session:
        if request.method=="GET":
            dprt_edit= DEPARTMENT.objects.get(id = pk)
            return render (request,"department_edit.html",{"dprt_edit":dprt_edit})
        elif request.method=="POST":
            
            Name=request.POST['name']
            Description=request.POST['description']

            dprt_edit= DEPARTMENT.objects.get(id = pk)
            dprt_edit.Name=Name
            dprt_edit.Description=Description
            dprt_edit.save()
            return redirect('department')
        else:
            return render(request,"login.html")
    else:
        return render(request,"login.html")    

def delete_department(request,pk):
    if 'id'  in request.session:
        dprt_delete= DEPARTMENT.objects.get(id = pk)
        print("-------------",dprt_delete)
        dprt_id=USER.objects.filter(Department=dprt_delete)
        print("_________________",dprt_id)
        if dprt_delete != dprt_id:
            dprt_delete= DEPARTMENT.objects.get(id = pk)
            dprt_delete.delete() 
            return redirect('department')
        else:
            e_msg="this Department not Deleted" 
            AllDepartment=DEPARTMENT.objects.all()
            return render(request,"department.html",{"AllDepartment":AllDepartment,'e_msg':e_msg})
    else:
        return render(request,"login.html")
