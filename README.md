## Snippets Module
**Custom file handlers and deployable ETL snippets for small projects**


### Archives
Early work on archive handling - giving flexible API for ETL pipelines to natively work with objects within compressed files.

**Example Usage**
import archives

> Test 1A: make an instance and manually set format
a = archives.Archive()
a.set_format('zip')
print('a format', a.format)
print('a path', a.path)

> Test 1B: make an instance with path to .zip file
b = archives.Archive(path='snippets.zip')
print('b path', b.path)
print('b format', b.format)

> Test 1C: make an instance with path to directory (default)
c = archives.Archive()
print('c path', c.path)
print('c format', c.format)

> Test 2A: Scan zip file
print('Scan of b, a zip file')
b.scan()

> Test 2B: Scan directory
print('Scan of c, a directory')
c.scan()