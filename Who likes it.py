'''Details:
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
My solution:
  '''
  def likes(name):
    if not name:
        return 'no one likes this'
    if len(name) == 1:
        return '{} likes this'.format(name[0])
    if len(name) == 2:
        return '{} and {} like this'.format(name[0],name[1])
    if len(name) == 3:
        return '{}, {} and {} like this'.format(name[0],name[1],name[2])
    if len(name) > 3:
        return '{}, {} and {} others like this'.format(name[0],name[1],len(name)-2)
