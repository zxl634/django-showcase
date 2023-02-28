# django-showcase

Example Django project to showcase serialization and create/save manipulation.

Gets an example usage of a word upon save from OpenAI API.

Data can then be retrieved in JSON with a call to for instance `http://localhost:8000/showcaseapp/fastidious/`.

Start server with `local/run.sh`.

Requires `.env` file with the following keys:

OPENAI_API_KEY=
SECRET_KEY=
DEBUG=

## Possible extensions

- [ ] Use OpenAI to translate the prompt depending on language
- [ ] Create word if not already in DB when trying to get word from endpoint.
- [ ] Sanitize JSON from endpoint further (e.g. only return fields)
