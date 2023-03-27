
		const form = document.querySelector('form');
		const successMessage = document.querySelector('.success-message');

		form.addEventListener('submit', function(event) {
			event.preventDefault(); // prevent the form from submitting normally

			// send the form data to the server using AJAX
			const xhr = new XMLHttpRequest();
			xhr.open('GET', 'action.php');
			xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
			xhr.onreadystatechange = function() {
				if (xhr.readyState === 4 && xhr.status === 200) {
					// show the success message if the form submission was successful
					successMessage.style.display = 'block';
				}
			};
			xhr.send(new FormData(form));
		});
