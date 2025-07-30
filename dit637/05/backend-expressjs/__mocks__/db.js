const mongoose = {
    connect: jest.fn(() => Promise.resolve()),
    connection: {
      close: jest.fn(() => Promise.resolve())
    }
  };
  
  export default mongoose;
  