module.exports =  function(arr) 
{
	for(j=1; j<arr.length;j++)
	{
		key = arr[j];
		i = j - 1;
		while(i>=0 && arr[i]>key) {
			arr[i+1] = arr[i];
			i--;
		}
		arr[i+1] = key;
	}
	return arr;
}

// randomArray = (length) => [...new Array(length)].map(() => Math.round(Math.random() * length));


