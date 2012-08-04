class AuthorsController < ApplicationController

  def show
    @author = Author.find(params[:id])
  end
  
  def new
    @author = Author.new
  end
  
  def create
    @author = Author.new(params[:author])
    if @author.save
      flash[:success] = "Created " + @author.full_name
      redirect_to @author
    else
      render 'new'
    end
  end
end
