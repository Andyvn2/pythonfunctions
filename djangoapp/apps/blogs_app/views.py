from django.shortcuts import render, HttpResponse, redirect


def index(request):
	response = "Placeholder to later display all the list of Coureses and descriptions"
	print request.session['name']
	return render(request, "blogs_app/index.html")



# def news(request):
# 	response = "Placeholder for a new post"
# 	return HttpResponse(response)


# def create(request):
# 	print "create initiate"
# 	if request.method == "POST":
# 		print "*"*50
# 		print request.POST['name']
# 		print request.POST['desc']
# 		request.session['name']= request.POST['name']
# 		print '*'*50
# 		print request.session['name']
# 		return redirect('/')
# 	else:
# 		return redirect('/')



	# 	print "*"*50
	# 	print request.POST
 #        print request.POST['name']
 #        print request.POST['desc']
 #        request.session['name'] = "test"  # more on session below
	# 	print "*"*50
	# 	return redirect("/")
	# else:
	# 	return redirect("/")


# def show(request, number):
# 	print "running request"
# 	response = "Place holder to display blog" +" " ,  number
# 	return HttpResponse(response)

# def edit(request, number):
# 	print "running request edit"
# 	response = "Place holder to edit blog" + " ", number
# 	return HttpResponse(response)
 

# def destroy(request, number):
# 	return redirect("/")