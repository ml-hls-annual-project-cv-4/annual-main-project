import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import 'bootstrap/dist/css/bootstrap.css';


function Navbar1() {
  return (
    <div className='left-20 absolute top-3 w-4/5 mx-auto'>
    <Navbar bg="light" expand="md" className='rounded-xl'>  
    <Container>  
      <Navbar.Brand href="#home">CV-Cars-4</Navbar.Brand>  
      <Navbar.Toggle aria-controls="basic-navbar-nav" />  
      <Navbar.Collapse id="basic-navbar-nav">  
        <Nav className="me-auto">  
          <Nav.Link href="/">Главная</Nav.Link>  
          <Nav.Link href="/dataset">О датасете</Nav.Link>
          <Nav.Link href="/prediction">Предсказать фото</Nav.Link>  
        </Nav>  
      </Navbar.Collapse>  
    </Container>  
  </Navbar>
  </div>
  );
}

export default Navbar1;