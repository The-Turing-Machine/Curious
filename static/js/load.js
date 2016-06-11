
var timer = 30;

function main()
{
    $.get('data',
    	function(data, status)
    	{
            // $('.subheading').html(data)
            console.log(data)
    	}
    );
}

var id = setInterval(main,timer);
