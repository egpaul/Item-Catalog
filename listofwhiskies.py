from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, BookDB, User

engine = create_engine('sqlite:///WhiskeyCatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy description the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="eric.paul@me.com")
session.add(User1)
session.commit()

# Whiskey data
whiskey1 = WhiskeyDB(WhiskeyName="Makers Mark",
                     avgPrice="$37.99",
                     description="Maker's Mark is a small-batch bourbon\
                     whiskey produced in Loretto, Kentucky, by Beam Suntory.\
                     It is bottled at 90 U.S. proof (45% alcohol by volume)\
                     and sold in distinctively squarish bottles sealed with\
                     red wax. The distillery offers tours, and is part of the\
                     American Whiskey Trail and the Kentucky Bourbon Trail.",
                     category="Bourbon", user_id=1)

session.add(whiskey1)
session.commit()

whiskey2 = WhiskeyDB(WhiskeyName="Woodford Reserve",
                     avgPrice="$44.99",
                     description="Woodford Reserve is a brand of premium small\
                     batch Kentucky straight bourbon whiskey produced in\
                     Woodford County, Kentucky by the Brown-Forman\
                     Corporation. It is made from a mixture of pot still\
                     spirits produced at the company's Woodford Reserve\
                     Distillery there, and column still spirits from the Brown\
                     Forman Distillery in Shively, Kentucky.",
                     category="Bourbon", user_id=1)

session.add(whiskey2)
session.commit()

whiskey3 = WhiskeyDB(WhiskeyName="Blanton's",
                     avgPrice="$59.99",
                     description="Blanton's is a brand of bourbon whiskey\
                     produced and marketed by the Sazerac Company. It is\
                     distilled in Frankfort, Kentucky at the Buffalo Trace\
                     Distillery.",
                     category="Bourbon", user_id=1)

session.add(whiskey3)
session.commit()

whiskey4 = WhiskeyDB(WhiskeyName="Jameson",
                     avgPrice="$32.99",
                     description="Jameson is a blended Irish whiskey produced\
                     by the Irish Distillers subsidiary of Pernod Ricard.",
                     category="Whiskey", user_id=1)

session.add(whiskey4)
session.commit()

whiskey5 = WhiskeyDB(WhiskeyName="Tullamore Dew",
                     avgPrice="$39.99",
                     description="Tullamore Dew is a brand of Irish whiskey\
                     produced by William Grant & Sons.[1] It is the second\
                     largest selling brand of Irish whiskey globally, with\
                     sales of over 950,000 cases per annum as of 2015",
                     category="Whiskey", user_id=1)

session.add(whiskey5)
session.commit()

whiskey6 = WhiskeyDB(WhiskeyName="Teeling",
                     avgPrice="$39.99",
                     description="Teeling Distillery is an Irish whiskey\
                     distillery established in Dublin in 2015. It is the first\
                     new whiskey distillery to have opened in Dubli",
                     category="Whiskey", user_id=1)

session.add(whiskey6)
session.commit()

whiskey7 = WhiskeyDB(WhiskeyName="Johnie Walker Black Label",
                     avgPrice="$33.99",
                     description="Johnnie Walker is a brand of Scotch whisky\
                     now owned by Diageo that originated in the Scottish town\
                     of Kilmarnock, East Ayrshire. The brand was first\
                     established by grocer John Walker.",
                     category="Scotch", user_id=1)

session.add(whiskey7)
session.commit()

whiskey8 = WhiskeyDB(WhiskeyName="The Macallan",
                     avgPrice="$54.99",
                     description="The Macallan distillery is a single malt\
                     Scotch whisky distillery in Craigellachie, Moray. The\
                     Macallan Distillers Ltd, is a wholly owned subsidiary of\
                     the Edrington Group which purchased the brand from\
                     Highland Distillers in 1999.",
                     category="Scotch", user_id=1)

session.add(whiskey8)
session.commit()

whiskey9 = WhiskeyDB(WhiskeyName="Laphroaig",
                     avgPrice="$46.99",
                     description="Laphroaig distillery is an Islay single malt\
                     Scotch whisky distillery. It is named for the area of\
                     land at the head of Loch Laphroaig on the south coast of\
                     the Isle of Islay. ",
                     category="Scotch", user_id=1)

session.add(whiskey9)
session.commit()

print "Enjoy your whiskey!"
