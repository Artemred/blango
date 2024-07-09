['/api/v1/posts/', '/', '/abadurl/'].forEach(url => {
  fetch(url).then(response => {
    if (response.status !== 200) {
      throw new Error('Invalid status from server: ' + response.statusText)
    }

    return response.json()
  }).then(data => {
    // do something with data, for example
    console.log(data)
  }).catch(e => {
    console.error(e)
  })
})