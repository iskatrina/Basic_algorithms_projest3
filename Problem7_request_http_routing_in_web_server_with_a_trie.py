# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler="Root Handler"):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for part in path:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for part in path:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node.handler

    
    
## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}


    def insert(self, path_part, handler=None):
         # Insert the node 
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode(handler)
        elif handler:
            self.children[path_part].handler = handler
            
            
 ## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler="Root Handler", not_found_response_handler="404 Not Found"):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.not_found_response_handler = not_found_response_handler
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)

        return handler if handler else self.not_found_response_handler
        
    
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [part for part in path.split('/') if part]

    
## Test cases:
## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


##My test cases:

## Test case1:
# Example usage:
router = Router()

# Adding handlers for different paths
router.add_handler("/", "home")
router.add_handler("/about me", "about me handler")
router.add_handler("/contact", "contact handler")
router.add_handler("/portfolio", "portfolio handler")
router.add_handler("/services/data scientist", "services data scientist handler")
router.add_handler("/services/game artist", "services game artist handler")

# Looking up handlers based on paths
print(router.lookup("/"))           # output: home 
print(router.lookup("/about me"))   # output: about me handler
print(router.lookup("/contact"))    # output: hontact handler
print(router.lookup("/portfolio"))       # output: portfolio handler
print(router.lookup("/services/data scientist"))  # output: services data scientist handler
print(router.lookup("/services/game artist"))  # output: services game artist handler
print(router.lookup("/unknown"))    # output: 404 Not Found


## Test case2:

# Example usage:
router = Router()

# Adding handlers for different paths
router.add_handler("/", "home")
router.add_handler("/1", "1 handler")
router.add_handler("/2", "2 handler")
router.add_handler("/3", "3 handler")
router.add_handler("/4/1", "4/1 handler")
router.add_handler("/4/2", "4/2 handler")

# Looking up handlers based on paths
print(router.lookup("/"))           # output: home 
print(router.lookup("/1"))   # output: 1 handler
print(router.lookup("/2"))    # output: 2 handler
print(router.lookup("/3"))       # output: 3 handler
print(router.lookup("/4/1"))  # output: 4/1 handler
print(router.lookup("/4/2"))  # output: 4/2 handler
print(router.lookup("/unknown"))    # output: 404 Not Found


## test case3:

# Example usage:
router = Router()

# Adding handlers for different paths
router.add_handler("/", "home")
router.add_handler("/about me/contact/portfolio/services/ds/artist/1/2/3/4/5/6/7/8/9/10", "about me, contact, portfolio,services, ds, artist /1/2/3/4/5/6/7/8/9/10 handler ")

# Looking up handlers based on paths
print(router.lookup("/"))           # output: home 
print(router.lookup("/about me/contact/portfolio/services/ds/artist/1/2/3/4/5/6/7/8/9/10"))   # output: about me, contact, portfolio,services, ds, artist /1/2/3/4/5/6/7/8/9/10 handler 


