import string
from Own_Cipher.src.cipher import Cipher

alphabet = string.ascii_letters

encoded = Cipher.encode(
    "Tyger Tyger, burning bright,  In the forests of the night;  What immortal hand or eye,  Could frame thy fearful symmetry?  In what distant deeps or skies.  Burnt the fire of thine eyes? On what wings dare he aspire? What the hand, dare seize the fire?  And what shoulder, & what art, Could twist the sinews of thy heart? And when thy heart began to beat, What dread hand? & what dread feet?  What the hammer? what the chain,  In what furnace was thy brain? What the anvil? what dread grasp,  Dare its deadly terrors clasp!   When the stars threw down their spears  And water'd heaven with their tears:  Did he smile his work to see? Did he who made the Lamb make thee?  Tyger Tyger burning bright,  In the forests of the night:  What immortal hand or eye, Dare frame thy fearful symmetry?",
    'mental')
print(encoded)
decoded = Cipher.decode(encoded, 'mental')
print(decoded)

text = """I promised to look after a friends cat for the week. My place has a glass atrium that goes through two 
levels, I have put the cat in there with enough food and water to last the week. I am looking forward to the end of 
the week. It is just sitting there glaring at me, it doesn't do anything else. I can tell it would like to kill me. 
If I knew I could get a perfect replacement cat, I would kill this one now and replace it Friday afternoon. As we sit 
here glaring at each other I have already worked out several ways to kill it. The simplest would be to drop heavy 
items on it from the upstairs bedroom though I have enough basic engineering knowledge to assume that I could build 
some form of 'spear like' projectile device from parts in the downstairs shed. If the atrium was waterproof, 
the most entertaining would be to flood it with water. It wouldn't have to be that deep, just deeper than the cat. I 
don't know how long cats can swim but I doubt it would be for a whole week. If it kept the swimming up for too long I 
could always try dropping things on it as well. I have read that drowning is one of the most peaceful ways to die so 
really it would be a win win situation for me and the cat I think """

text_enc = Cipher.encode(text, "tjach")
print(text_enc)
