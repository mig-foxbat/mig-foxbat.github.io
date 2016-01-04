Title: Directives Scopes
Tags: AngularJS 
Author: Charles
Summary: scopes in AngularJS Directives
Date: 2015-05-16

In this blog post we will discuss about scopes in AngularJS Directives. This post assumes you have atleast beginner level knowledge on AngularJS. By beginner level I mean you would know what are scopes, Directives and its basic structure.

By default, Directives inherit the scope of its containing Controller(s). This scope is passed as an argument in the link function of the Directive as shown below

```
function($scope, $element, $attrs) {  // These arguments are not dependency injected and hence their position matters.
}

  /*
  	The three attributes passed are 
  	scope: The effective scope of Controller(s) that is enclose to the Directive.
  	element: jqlite element object of the Directive. in this its something like this angular.element("<my-custom-Directive param1=\"value1\" param2=\"{{a_Controller_variable}}\">")
  	attrs: an helper object with all the html attributes defined as its object attribute
  */


```

One of the most important design principle with Directives is that they are supposed to be independent reusable entities and should not have hard dependencies with Controllers. A lousy developer might read scope attributes values directly off the scope object passed in the link function which will lead to a situation where you must always use this Directive with a specific Controller that defines that specific attribute. The better way to pass data between Controller scope and link function of a Directive is to pass the data via attributes of the Directive as shown below.

```
  <my-custom-Directive param1="value1" param2="{{a_controller_variable}}"> // in HTML

  ...             // in Directive definition
  link: function(scope,element,attrs) {     
  	var a1 = attrs.param1
  	// do some DOM manipulation 
  }
  ...

```

However there is one big darn flaw with the above approach. The Directive link function has no way to track changes to the attribute value. If the value of the `a_controller_variable` changes the Directive would not react to this change and hence there is virtually no binding between the Controller and the Directive. One possible solution is to use the `$observer` function in attrs as shown below. In this method we register for any changes that happens to the attribute param2 and on change of this attribute we can execute our custom function passed as second parameter to `$observer`

```
link: function(scope,element,attrs) {
	attrs.$observe('param2',function(value){ 
		// do some processing with value parameter
	})
}
```

But this is not an elegant solution and the scope key in the Directive definition comes to save the day. The scope key in Directive definition takes any of the following values

* `false` : This is the default value. This makes the Directive to get a reference the Controller scope to which it is bound.
* `true` : This creates a new scope for the Directive but this new scope inherits the Controller scope to which the Directive is bound. Thus the Directive can access all the Controller scope attributes but it cannot overwrite any of those inherited attributes (a kind of one-way binding)
* `{}` : (i.e. an empty object): This creates a new scope for the Directive which is completely insulted with its Controller scope object. in AngularJS this is called an isolate scope.

###### Isolated scope:

  Isolate scope is the one we are going to explore now since it is the most recommended way to create re-usable Directive. As said earlier isolated scopes are almost completely insulated from Controller scope and don't share data betweem them. But this would make Directives un-configurable and monotonous. To address this isolate scope provides means to pass configurable data to Directives via attributes. This is achieved by providing key value pairs to the isolate scope object. for example see the example below

```
  <my-custom-Directive key1="{{ctrl.var}}" key2="ctrl.obj" key3="ctrl.func()">

  key: {
  	'key1': '@',
  	'key2': '=',
  	'key3': '&'
  }
```

Lets discuss each of the symbols defined above

* `@` : The `@` symbol means that the value provided to the key1 attribute must be a expression that should resolve to a string. It can be a Controller attribute which resolves To a string value as shown above or a plain string like `key="xyz"`. Use this if you want one way binding between your Controller and Directive in the direction of from Controller to Directive. 

* `=` : This means that the Directive attribute holds reference to a JSON object usually which is inside the scope object of the Controller. This object reference is passed down to the Directive's isolate scope. The key point is that now both Controller scope and Directive scope has reference to the same JSON object and hence this can be used for two way binding between the Controller and the Directive.

* `'&'` : This is similar to the `=` sign but instead of passing a reference of a JSON object in Controller scope, a function reference is passed down. The Directive then can invoke this Controller function when required.


