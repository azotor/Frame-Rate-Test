import pygame, sys, math

pygame.init()

class Game:
    def __init__( self ):
        
        self.surf = pygame.display.set_mode( ( 800, 600 ) )
        pygame.display.set_caption( "FPS TEST" )
        self.run = True
        self.clock = pygame.time.Clock()
        self.lastTime = pygame.time.get_ticks()
        self.delay = 0
        self.fps = 60
        self.pos = ( 400, 300 )
        self.angle = 0
        self.angleInc = .002
        self.length = 100
        
        self.loop()
    
    def loop( self ):
        
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.fps += 10
                    if event.key == pygame.K_DOWN:
                        self.fps -= 10
                        if self.fps <= 0:
                            self.fps = 10
                    if event.key == pygame.K_LEFT:
                        self.angleInc = self.angleInc - .001
                        if self.angleInc <= 0:
                            self.angleInc = .001
                    if event.key == pygame.K_RIGHT:
                        self.angleInc = self.angleInc + .001
                    if event.key == pygame.K_EQUALS:
                        self.length += 10
                        if self.length >= 200:
                            self.length = 200
                    if event.key == pygame.K_MINUS:
                        self.length -= 10
                        if self.length <= 50:
                            self.length = 50
                    if event.key == pygame.K_SPACE:
                        self.fps = 60
                        self.angleInc = .002
                        self.length = 100

            now = pygame.time.get_ticks()
            self.delay = now - self.lastTime
            self.lastTime = now

            self.update()
            self.render()
            self.clock.tick( self.fps )
            
        pygame.quit()
        sys.exit()
    
    def update( self ):
        self.angle += self.angleInc * ( 1000 / self.fps )
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi
        if self.angle < 0:
            self.angle += 2 * math.pi
    
    def render( self ):
        self.surf.fill( "#222222" )
        if self.delay > 0:
            font_big = pygame.font.SysFont( "verdana", 24 )
            font_small = pygame.font.SysFont( "verdana", 14 )
            text = font_big.render( "FPS: " + str( 1000 // self.delay ) + " ( " + str( self.fps ) + " )", True, "white" )
            text_rect = text.get_rect( topleft = ( 10, 10 ) )
            self.surf.blit( text, text_rect )
            text = font_big.render( "AngleInc: " + str( round( self.angleInc, 4 ) ) + " rad", True, "white" )
            text_rect = text.get_rect( topleft = ( 10, 40 ) )
            self.surf.blit( text, text_rect )
            text = font_big.render( "Angle: " + str( round( self.angle, 4 ) ) + " rad", True, "white" )
            text_rect = text.get_rect( topleft = ( 10, 70 ) )
            self.surf.blit( text, text_rect )
            text = font_big.render( "Length: " + str( self.length ), True, "white" )
            text_rect = text.get_rect( topleft = ( 10, 100 ) )
            self.surf.blit( text, text_rect )
            
            text = font_small.render( "up : +10 FPS", True, "white" )
            text_rect = text.get_rect( topright = ( self.surf.get_width() - 10, 10 ) )
            self.surf.blit( text, text_rect )
            text = font_small.render( "down : -10 FPS", True, "white" )
            text_rect = text.get_rect( topright = ( self.surf.get_width() - 10, 30 ) )
            self.surf.blit( text, text_rect )
            text = font_small.render( "left : -0.001 angle", True, "white" )
            text_rect = text.get_rect( topright = ( self.surf.get_width() - 10, 50 ) )
            self.surf.blit( text, text_rect )
            text = font_small.render( "right : +0.001 angle", True, "white" )
            text_rect = text.get_rect( topright = ( self.surf.get_width() - 10, 70 ) )
            self.surf.blit( text, text_rect )
            text = font_small.render( "plus : +10 length", True, "white" )
            text_rect = text.get_rect( topright = ( self.surf.get_width() - 10, 90 ) )
            self.surf.blit( text, text_rect )
            text = font_small.render( "minus : -10 length", True, "white" )
            text_rect = text.get_rect( topright = ( self.surf.get_width() - 10, 110 ) )
            self.surf.blit( text, text_rect )
            text = font_small.render( "space : reset", True, "white" )
            text_rect = text.get_rect( topright = ( self.surf.get_width() - 10, 130 ) )
            self.surf.blit( text, text_rect )
        
        x = self.pos[ 0 ] + math.cos( self.angle ) * self.length
        y = self.pos[ 1 ] + math.sin( self.angle ) * self.length
        pygame.draw.line( self.surf, 'white', ( self.pos + pygame.math.Vector2( -10, 0 ) ), ( self.pos + pygame.math.Vector2( 10, 0 ) ) )
        pygame.draw.line( self.surf, 'white', ( self.pos + pygame.math.Vector2( 0, -10 ) ), ( self.pos + pygame.math.Vector2( 0, 10 ) ) )
        pygame.draw.line( self.surf, 'orange', self.pos, ( x, y ), 2 )
        pygame.draw.circle( self.surf, "#ff0088", ( x, y ), 20 )
        
        pygame.display.update()
        