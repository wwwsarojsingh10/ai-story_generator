const storyForm = document.querySelector('#story-form');
const storyDiv = document.querySelector('#story');

storyForm.addEventListener('submit', e => {
	e.preventDefault();
	const promptInput = document.querySelector('#prompt').value;
print("bchgfhxfgb")
	// validate user input
	if (promptInput.trim() === '') {
		alert('Please enter a prompt or keywords.');
		return;
	}

	// send user input to backend
	fetch('/generate', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ prompt: promptInput })
	})
	.then(res => res.json())
	.then(data => {
		// display generated story to user
		storyDiv.innerHTML = `<p>${data.story}</p>`;
	})
	.catch(err => console.log(err));
});
